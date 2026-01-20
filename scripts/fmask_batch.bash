#!/bin/bash

num_cpus=$(nproc --all)

fmask_batch() {
    local in_dir="data/in"
    local out_dir="data/out/HI/$1/$5/$2_$3_$4"
    [ ! -d $out_dir ] && mkdir -p $out_dir

    for i in $(seq 1 $num_cpus); do
        PHY_CONST_SRC=$5 python main/fmask_batch.py --ci $i --cn $num_cpus \
            --model $1 --dcloud $2 --dshadow $3 --dsnow $4 \
            --imagedir $in_dir --output $out_dir --skip_existing yes --save_metadata no --display_fmask no --display_image no --print_summary yes &
    done
    wait
}

fmask_batch PHY 0 5 0 constant
fmask_batch PHY 1 2 0 constant
fmask_batch PHY 1 2 0 constant_water
fmask_batch UPL 0 5 0 constant
fmask_batch UPL 1 2 0 constant
fmask_batch UPL 1 2 0 constant_water
fmask_batch UPU 0 5 0 constant
fmask_batch UPU 1 2 0 constant
fmask_batch UPU 1 2 0 constant_water
