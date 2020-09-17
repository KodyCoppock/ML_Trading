library(tidyverse)
library(stringr)
library(magrittr)

list_of_files <- list.files(path = "D:\\75752_1304789_bundle_archive\\full_history",
                            full.names = TRUE)
df <- list_of_files %>%
  setNames(nm = .) %>% 
  map_df(~read_csv(.x, col_types = cols(), col_names = FALSE), .id = "file_name")

write.csv(df, file = "combined_stock_data.csv")

