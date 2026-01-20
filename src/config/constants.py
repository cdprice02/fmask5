"""
Constant values that will not change from run to run.
"""

CONSTANTS = {
    # The smallest positive float in order to avoid division by zero
    # float16: 0.000977
    # float32: 1.19209e-07
    # float64: 2.220446049250313e-16
    "EPS": 1.19209e-07,
    # Label values
    "LABEL_LAND": 0,
    "LABEL_CLEAR": 0,
    "LABEL_WATER": 1,
    "LABEL_SHADOW": 2,
    "LABEL_SNOW": 3,
    "LABEL_CLOUD": 4,
    "LABEL_FILL": 255,
    # GSWO coordinates
    "NORTH_LAT_GSWO": 78,
    "SOUTH_LAT_GSWO": -59,
    # Random seed for reproducability
    "RANDOM_SEED": 42,
    # URLs for the large files such as GSWO, GT30, and UNet model, which cannot be uploaded to the GitHub
    "URL_global_gswo150": "https://drive.google.com/file/d/13JIxS9j1lsxZQnYEgjdhHxk7Z3Cqcbeq/view?usp=drive_link",
    "URL_global_gt30": "https://drive.google.com/file/d/1IhsVi5FKxqEyVs2Vc0F_sg48EIjVekGt/view?usp=drive_link",
    "URL_unet_ncf_l7": "https://drive.google.com/file/d/1A_cd05CvgRzmiXr_nNhg5yHLS5zpzR6t/view?usp=drive_link",
    "URL_unet_ncf_l8": "https://drive.google.com/file/d/1yysrwxgk8Y6IHPTnvIFHChEEgEfrZTow/view?usp=drive_link",
    "URL_unet_ncf_s2": "https://drive.google.com/file/d/1GpwtS5cZ90NvmLvrtD9jT8X7vCQKd6i_/view?usp=drive_link",
}
