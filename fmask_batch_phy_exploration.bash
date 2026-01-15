#!/bin/bash
fmask_batch() {
    local in_dir="data/in"
    local out_dir="data/out/HI/$1/$5/$2_$3_$4"
    [ ! -d $out_dir ] && mkdir -p $out_dir

    PHY_CONST_SRC=$5 python main/fmask_batch.py --model $1 --dcloud $2 --dshadow $3 --dsnow $4 --imagedir $in_dir --output $out_dir --skip_existing yes --save_metadata no --display_fmask no --display_image no --print_summary yes
    return $? && tar -cvzf "${out_dir}.tar.gz" $out_dir
}

fmask_batch PHY 0 5 0 constant
fmask_batch PHY 1 2 0 constant
fmask_batch PHY 1 2 0 constant_water
fmask_batch UPL 0 5 0 constant
fmask_batch UPL 1 2 0 constant
fmask_batch UPL 1 2 0 constant_water
