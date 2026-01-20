#!/bin/bash

#SBATCH --job-name=fmask-phy
#SBATCH --output=fmask_%j_%a.out
#SBATCH --account=eros
#SBATCH --time=2:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem-per-cpu=16G
#SBATCH --array=0-7

FIELDS_COUNT=5
TASKS=(
    "PHY" "3" "5" "0" ""
    "PHY" "3" "5" "0" "config/water_1.json"
    "PHY" "3" "5" "0" "config/water_2.json"
    "PHY" "3" "5" "0" "config/water_3.json"
    "UPL" "3" "5" "0" ""
    "UPL" "3" "5" "0" "config/water_1.json"
    "UPL" "3" "5" "0" "config/water_2.json"
    "UPL" "3" "5" "0" "config/water_3.json"
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
    local config_path="$5"
    local in_dir="./data/in"
    local out_dir="./data/out/HI/${model}"

    unset CONFIG_FILE_PATH
    if [ "${config_path}" -ne "" ]; then
        export CONFIG_FILE_PATH=${config_path}
        out_dir+="/$(basename ${config_path%.*})"
    fi

    out_dir+="/${dcloud}_${dshadow}_${dsnow}"

    [ ! -d $out_dir ] && mkdir -p $out_dir

    for i in $(seq 1 $SLURM_CPUS_PER_TASK); do
        python main/fmask_batch.py --ci $i --cn $SLURM_CPUS_PER_TASK \
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
config_path=${TASKS[$INDEX+4]}

fmask_batch $model $dcloud $dshadow $dsnow $config_path
