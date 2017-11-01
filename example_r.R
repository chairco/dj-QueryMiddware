# Example for r to curl the data from Restful web service
# client should install.packages('curl') 
# packages fromJSON is default install after R 3.3.3 

# get one glassid from rest
baseurl <- "http://localhost:8000/autosearch/edch/?glassid="
res <- fromJSON(paste0(baseurl, "TL6AS0KAF"), flatten=True)
stepid <- res$STEP_ID
