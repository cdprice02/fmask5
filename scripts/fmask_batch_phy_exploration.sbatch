#!/bin/bash

#SBATCH --job-name=fmask-phy
#SBATCH --output=fmask_%j_%a.out
#SBATCH --account=eros
#SBATCH --time=1:00:00
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=16G
#SBATCH --array=0-8

FIELDS_COUNT=5
TASKS=(
    "PHY" "0" "5" "0" "constant"
    "PHY" "1" "2" "0" "constant"
    "PHY" "1" "2" "0" "constant_water"
    "UPL" "0" "5" "0" "constant"
    "UPL" "1" "2" "0" "constant"
    "UPL" "1" "2" "0" "constant_water"
    "UPU" "0" "5" "0" "constant"
    "UPU" "1" "2" "0" "constant"
    "UPU" "1" "2" "0" "constant_water"
)

NUM_TASKS=$((${#TASKS[@]} / FIELDS_COUNT))
if [ "$SLURM_ARRAY_TASK_MAX" -ne $((NUM_TASKS - 1)) ]; then
    echo "Error: --array=0-$SLURM_ARRAY_TASK_MAX does not match the number of tasks (${NUM_TASKS} in TASKS array)."
    echo "Expected --array range: 0-$((NUM_TASKS - 1))"
    exit 1
fi

fmask_batch() {
    local model="$1"
    local dcloud="$2"
    local dshadow="$3"
    local dsnow="$4"
    local constant="$5"

    local in_dir="./data/in"
    local out_dir="./data/out/HI/${model}/${constant}/${dcloud}_${dshadow}_${dsnow}"

    [ ! -d $out_dir ] && mkdir -p $out_dir

    for i in $(seq 1 $SLURM_CPUS_PER_TASK); do
        PHY_CONST_SRC=${constant} python "./main/fmask_batch.py" --ci $i --cn $SLURM_CPUS_PER_TASK \
            --model ${model} --dcloud ${dcloud} --dshadow ${dshadow} --dsnow ${dsnow} \
            --imagedir $in_dir --output $out_dir --skip_existing no --save_metadata no \
            --display_fmask no --display_image no --print_summary yes &
    done

    wait
}

INDEX=$((SLURM_ARRAY_TASK_ID * FIELDS_COUNT))
model=${TASKS[$INDEX]}
dcloud=${TASKS[$INDEX+1]}
dshadow=${TASKS[$INDEX+2]}
dsnow=${TASKS[$INDEX+3]}
constant=${TASKS[$INDEX+4]}

fmask_batch $model $dcloud $dshadow $dsnow $constant
