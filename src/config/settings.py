import json
import os


def load_config_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")

    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f"Error loading config file {file_path}: {e}")


config_file_path = os.getenv("CONFIG_FILE_PATH", None)
external_settings = load_config_file(config_file_path) if config_file_path else {}

SETTINGS = {
    "MSG_BASE": external_settings.get("MSG_BASE", True),
    "MSG_FULL": external_settings.get("MSG_FULL", True),
    "LOW_LEVEL": external_settings.get("LOW_LEVEL", 17.5),  # low percentile (see Zhu and Curtis, 2012)
    "HIGH_LEVEL": external_settings.get("HIGH_LEVEL", 82.5),  # high percentile (see Zhu and Curtis, 2012)
    "PHY_PCP_NDVI_UPPER_LIMIT": external_settings.get("PHY_PCP_NDVI_UPPER_LIMIT", 0.8),
    "PHY_PCP_NDSI_UPPER_LIMIT": external_settings.get("PHY_PCP_NDSI_UPPER_LIMIT", 0.8),
    "PHY_PCP_SWIR2_LOWER_LIMIT": external_settings.get("PHY_PCP_SWIR2_LOWER_LIMIT", 0.03),
    "PHY_PCP_TIRS_UPPER_LIMIT": external_settings.get("PHY_PCP_TIRS_UPPER_LIMIT", 27),  # in degrees
    "PHY_PCP_WHITENESS_UPPER_LIMIT": external_settings.get("PHY_PCP_WHITENESS_UPPER_LIMIT", 0.7),
    "PHY_PCP_HOT_LOWER_LIMIT": external_settings.get("PHY_PCP_HOT_LOWER_LIMIT", 0),
    "PHY_PCP_4_5_LOWER_LIMIT": external_settings.get("PHY_PCP_4_5_LOWER_LIMIT", 0.75),
    "PHY_SNOW_NDSI_LOWER_LIMIT": external_settings.get("PHY_SNOW_NDSI_LOWER_LIMIT", 0.15),
    "PHY_SNOW_NIR_LOWER_LIMIT": external_settings.get("PHY_SNOW_NIR_LOWER_LIMIT", 0.11),
    "PHY_SNOW_GREEN_LOWER_LIMIT": external_settings.get("PHY_SNOW_GREEN_LOWER_LIMIT", 0.1),
    "PHY_SNOW_TIRS_UPPER_LIMIT": external_settings.get("PHY_SNOW_TIRS_UPPER_LIMIT", 10),  # in degrees
    "PHY_ABS_SNOW_UPPER_LIMIT": external_settings.get("PHY_ABS_SNOW_UPPER_LIMIT", 0.0009),
    "PHY_WATER_A_NDVI_LOWER_LIMIT": external_settings.get("PHY_WATER_A_NDVI_LOWER_LIMIT", 0),
    "PHY_WATER_A_NDVI_UPPER_LIMIT": external_settings.get("PHY_WATER_A_NDVI_UPPER_LIMIT", 0.1),
    "PHY_WATER_A_NIR_UPPER_LIMIT": external_settings.get("PHY_WATER_A_NIR_UPPER_LIMIT", 0.05),
    "PHY_WATER_B_NDVI_UPPER_LIMIT": external_settings.get("PHY_WATER_B_NDVI_UPPER_LIMIT", 0.01),
    "PHY_WATER_B_NIR_UPPER_LIMIT": external_settings.get("PHY_WATER_B_NIR_UPPER_LIMIT", 0.11),
    "PHY_CIRRUS_MULT": external_settings.get("PHY_CIRRUS_MULT", 25),
    "PHY_LAND_TEMP_SPAN": external_settings.get("PHY_LAND_TEMP_SPAN", 4),  # in degrees
    "PHY_WATER_TEMP_MULT": external_settings.get("PHY_WATER_TEMP_MULT", 0.25),
    "PHY_WATER_BRIGHTNESS_MULT": external_settings.get("PHY_WATER_BRIGHTNESS_MULT", 1 / 0.11),
    "PHY_LAND_BRIGHTNESS_SPAN": external_settings.get("PHY_LAND_BRIGHTNESS_SPAN", 0.04),
    "PHY_SHADOW_FLOOD_FILL_THRESHOLD_1": external_settings.get("PHY_SHADOW_FLOOD_FILL_THRESHOLD_1", 0.15),
    "PHY_SHADOW_FLOOD_FILL_THRESHOLD_2": external_settings.get("PHY_SHADOW_FLOOD_FILL_THRESHOLD_2", 0.02),
    "PHY_CIRRUS_LOWER_LIMIT": external_settings.get("PHY_CIRRUS_LOWER_LIMIT", 0.01),
    "PHY_COLD_CLOUD_THRESHOLD": external_settings.get("PHY_COLD_CLOUD_THRESHOLD", 35),  # in degrees
}
