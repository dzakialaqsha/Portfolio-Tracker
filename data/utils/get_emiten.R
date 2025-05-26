#############################################################################################
#                                   IMPORTING STOCKS LIST                                   #
#############################################################################################
# URL : https://id.wikipedia.org/wiki/Daftar_perusahaan_yang_tercatat_di_Bursa_Efek_Indonesia                             
#
#############################################################################################
install.packages("rvest")
install.packages("curl")
install.packages("tidyverse")
install.packages("stringr")

library(rvest)
library(curl) #TO modify browser agent like behavior, i suppose
library(tidyverse)
library(stringr)

################################################################################
#  Web Scraping Daftar Emiten
################################################################################

#####################
# 1. Get list
#####################

url_link <- "https://id.wikipedia.org/wiki/Daftar_perusahaan_yang_tercatat_di_Bursa_Efek_Indonesia"

page <- rvest::read_html(curl(url_link, handle = curl::new_handle("useragent" = "Mozilla/5.0")))  

emiten_data <- page %>% html_element(xpath = '//*[@id="mw-content-text"]/div[1]/table') %>% html_table()

#####################
# 2. Data Formatting
#####################
#initiate empty df
cl_emiten_data <- data.frame(
  code = substr(emiten_data$Kode, nchar(emiten_data$Kode) - 3, nchar(emiten_data$Kode)),
  name = emiten_data$`Nama perusahaan`,
  ipo_date = str_match(emiten_data$`Tanggal pencatatan`, "\\((\\d{4}-\\d{2}-\\d{2})\\)")[, 2],
  papan_pencatatan = emiten_data$`Papan pencatatan`,
  industry = emiten_data$Sektor
)

#save file in cwd
