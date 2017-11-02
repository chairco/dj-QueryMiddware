# Example for r to curl the data from Restful web service
# client should install.packages('curl') 
# packages fromJSON is default install after R 3.3.3 


library(jsonlite)
library(curl)

baseurl <- 'http://localhost:8000/autosearch/edch/?glassid='
glassid <- read.csv(file='sample-10.csv', header=FALSE)$V1
glassid <- as.character(glassid)
datas <- list()

# Sequence to get the glass data.
for (gid in glassid) {
  url <- paste0(baseurl, gid)
  res <- fromJSON(url)
  datas[[gid]] <- c(res)
  # Outut csv file by glassid.
  write.csv(res, paste0(gid, '.csv'))
}



