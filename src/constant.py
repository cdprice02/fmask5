"""constant.py: Constants for the Fmask5, whic"""

# The smallest positive float in order to avoid division by zero
# float16: 0.000977
# float32: 1.19209e-07
# float64: 2.220446049250313e-16
EPS = 1.19209e-07
LABEL_CLOUD = 4
LABEL_SNOW = 3
LABEL_SHADOW = 2
LABEL_WATER = 1
LABEL_LAND = 0
LABEL_CLEAR = 0
LABEL_FILL = 255
RANDOM_SEED = 42  # None: dynamic ||| 42 static seed for reproductivity A popular value chosen all over the world for the random state is 42. The reason was a little surprising and quirky. The number simply has been made popular by a comic science fiction called "The Hitchhiker's Guide to the Galaxy" authored by Douglas Adams in 1978
HIGH_LEVEL, LOW_LEVEL = 82.5, 17.5  # percentiles see Zhu and Curtis, 2012

NORTH_LAT_GSWO, SOUTH_LAT_GSWO = (
    78,
    -59,
)  # The north and south border of the GSWO, by examining the 30-m product. Any pixels within this range, the tool will not use the GSWO layer
MSG_BASE = True  # whether to show the base message
MSG_FULL = True  # whether to show the all message

# below variables are the URLs for the large files such as GSWO, GT30, and UNet model, which cannot be uploaded to the GitHub
URL_global_gswo150 = "https://drive.google.com/file/d/13JIxS9j1lsxZQnYEgjdhHxk7Z3Cqcbeq/view?usp=drive_link"
URL_global_gt30 = "https://drive.google.com/file/d/1IhsVi5FKxqEyVs2Vc0F_sg48EIjVekGt/view?usp=drive_link"
URL_unet_ncf_l7 = "https://drive.google.com/file/d/1A_cd05CvgRzmiXr_nNhg5yHLS5zpzR6t/view?usp=drive_link"
URL_unet_ncf_l8 = "https://drive.google.com/file/d/1yysrwxgk8Y6IHPTnvIFHChEEgEfrZTow/view?usp=drive_link"
URL_unet_ncf_s2 = "https://drive.google.com/file/d/1GpwtS5cZ90NvmLvrtD9jT8X7vCQKd6i_/view?usp=drive_link"
# physical model limits for PCP tests and more
PHY_PCP_NDVI_UPPER_LIMIT = 0.8
PHY_PCP_NDSI_UPPER_LIMIT = 0.8
PHY_PCP_SWIR2_LOWER_LIMIT = 0.03
PHY_PCP_TIRS_UPPER_LIMIT = 27  # in degrees
PHY_PCP_WHITENESS_UPPER_LIMIT = 0.7
PHY_PCP_HOT_LOWER_LIMIT = 0
PHY_PCP_4_5_LOWER_LIMIT = 0.75

PHY_SNOW_NDSI_LOWER_LIMIT = 0.15
PHY_SNOW_NIR_LOWER_LIMIT = 0.11
PHY_SNOW_GREEN_LOWER_LIMIT = 0.1
PHY_SNOW_TIRS_UPPER_LIMIT = 10  # in degrees

PHY_ABS_SNOW_UPPER_LIMIT = 0.0009

PHY_WATER_A_NDVI_LOWER_LIMIT = 0
PHY_WATER_A_NDVI_UPPER_LIMIT = 0.1
PHY_WATER_A_NIR_UPPER_LIMIT = 0.05
PHY_WATER_B_NDVI_UPPER_LIMIT = 0.01
PHY_WATER_B_NIR_UPPER_LIMIT = 0.11
# begin water adjustment code
PHY_WATER_USE_NDMI = False
PHY_WATER_A_NDMI_UPPER_LIMIT = 0.9
PHY_WATER_B_NDMI_UPPER_LIMIT = 0.9
# end water adjustment code

PHY_CIRRUS_MULT = 25
PHY_LAND_TEMP_SPAN = 4  # in degrees
PHY_WATER_TEMP_MULT = 0.25
PHY_WATER_BRIGHTNESS_MULT = 1 / 0.11
PHY_LAND_BRIGHTNESS_SPAN = 0.04
PHY_SHADOW_FLOOD_FILL_THRESHOLD_1 = 0.15
PHY_SHADOW_FLOOD_FILL_THRESHOLD_2 = 0.02
PHY_CIRRUS_LOWER_LIMIT = 0.01

PHY_COLD_CLOUD_THRESHOLD = 35  # in degrees
