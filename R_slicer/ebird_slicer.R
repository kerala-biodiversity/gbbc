library(tidyverse)
library(sf)

# We need to store a few things in config.R
# ebird_file - which is path to the ebird data file (.txt)
# iucn_file - which is path to the iucn data file (.csv)
source("config.R")

if (!file.exists(ebird_file)) {
  stop("Please add ebird_file to config.R with the path to ebird data .txt file")
}


read_ebird_file <- function (file) {
  columns_to_keep <- c(
    "COMMON NAME",
    "SCIENTIFIC NAME",
    "CATEGORY",
    "STATE CODE",
    "COUNTY CODE",
    "OBSERVATION DATE",
    "LAST EDITED DATE",
    "LOCALITY ID",
    "LATITUDE",
    "LONGITUDE",
    "SAMPLING EVENT IDENTIFIER",
    "ALL SPECIES REPORTED",
    "GROUP IDENTIFIER",
    "APPROVED",
    "DURATION MINUTES",
    "OBSERVER ID"
  )
  
  data <- read_tsv(file,
                   col_select = all_of(columns_to_keep),
                   lazy = TRUE)
  return (data)
}


data <- read_ebird_file(ebird_file)
# filtered_data <- filter_records(data)
data <- data
data2 <- subset(data, data["OBSERVATION DATE"] > start_date & data["OBSERVATION DATE"] < end_date)
