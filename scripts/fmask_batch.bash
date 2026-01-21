#!/bin/bash

num_cpus=$(nproc --all)

fmask_batch() {
    local model="$1"
    local dcloud="$2"
    local dshadow="$3"
    local dsnow="$4"
    local config_path="$5"
    local in_dir="./data/in"
    local out_dir="./data/out/HI/${model}"

    unset CONFIG_FILE_PATH
    if [ ! -z ${config_path} ]; then
        export CONFIG_FILE_PATH=${config_path}
        out_dir+="/$(basename ${config_path%.*})"
    else
        out_dir+="/default"
    fi

    out_dir+="/${dcloud}_${dshadow}_${dsnow}"

    [ ! -d $out_dir ] && mkdir -p $out_dir

    for i in $(seq 1 $num_cpus); do
        python main/fmask_batch.py --ci $i --cn $num_cpus \
            --model ${model} --dcloud ${dcloud} --dshadow ${dshadow} --dsnow ${dsnow} \
            --imagedir $in_dir --output $out_dir --skip_existing no --save_metadata no \
            --display_fmask no --display_image no --print_summary yes &
    done
    wait
}

fmask_batch PHY 3 5 0 ""
fmask_batch PHY 3 5 0 "config/water_1.json"
fmask_batch PHY 3 5 0 "config/water_2.json"
fmask_batch PHY 3 5 0 "config/water_3.json"
fmask_batch UPL 3 5 0 ""
fmask_batch UPL 3 5 0 "config/water_1.json"
fmask_batch UPL 3 5 0 "config/water_2.json"
fmask_batch UPL 3 5 0 "config/water_3.json"
