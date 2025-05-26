#############################################################################################
#                                   IMPORTING STOCKS LIST                                   #
#############################################################################################
# URL : https://id.wikipedia.org/wiki/Daftar_perusahaan_yang_tercatat_di_Bursa_Efek_Indonesia                             
#
#############################################################################################
# The script performs the following steps:
# 1. Checks for and installs (if necessary) required R packages.
# 2. Fetches the HTML content from the specified Wikipedia URL.
# 3. Extracts the main table containing emiten data using an XPath.
# 4. Formats and cleans the extracted data into a structured data frame.
# 5. Creates the output directory if it doesn't exist.
# 6. Saves the cleaned data as a CSV file to a predefined path.

packages <- c("rvest", "curl", "tidyverse", "stringr")

# Loop through the packages
for (pkg in packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    message(paste0("Installing package: ", pkg))
    install.packages(pkg)
  }
  library(pkg, character.only = TRUE) # Load the package
  message(paste0("Loaded package: ", pkg))
}

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

#####################
# 3. Save file to the specified path
#####################
output_file_path <- "/content/Portfolio-Tracker/data/list_emiten/list_emiten.csv"
output_directory <- dirname(output_file_path)

# Create the directory if it doesn't exist
# recursive = TRUE ensures all necessary parent directories are created
dir.create(output_directory, showWarnings = FALSE, recursive = TRUE)
message(paste0("Ensured output directory exists: ", output_directory))

write.csv(cl_emiten_data, file = output_file_path, row.names = FALSE)
