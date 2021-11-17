# Patrick L. Harvey
# CSYS 300
# Project (DRAFT)
# 20210929

library(ggplot2)
library(ggExtra)
library(hrbrthemes)
library(tidymodels)
library(tidyverse)
library(extrafont)
library(broom)
library(latex2exp)
library(hexbin)
library(RColorBrewer)
library(stats)

hrbrthemes::import_roboto_condensed()

# Use working directory below on main workstation
#setwd("C:/Users/pharv/Desktop/CSYS 300 (Principles of Complex Systems)/Project")

# Credit: Jack Aidley
# https://stackoverflow.com/questions/11610377/...
# how-do-i-change-the-formatting-of-numbers-on-an-axis-with-ggplot
fancy_scientific <- function(l) {
  # turn in to character string in scientific notation
  l <- format(l, scientific = TRUE)
  # quote the part before the exponent to keep all the digits
  l <- gsub("^(.*)e", "'\\1'e", l)
  # turn the 'e+' into plotmath format
  l <- gsub("e", "%*%10^", l)
  # return this as an expression
  parse(text=l)
}

# Import Data
# Data source: https://www.ers.usda.gov/webdocs/DataFiles/80526/...
# FoodEnvironmentAtlas.xls?v=7317.7
# Alternate: https://www.ers.usda.gov/webdocs/DataFiles/80526/...
# FoodEnvironmentAtlas.zip?v=7317.7
###var_list <- read.csv(file = 'Data/VariableList.csv', header = TRUE)
###var_code <- var_list$Variable_Code
FEA_whole <- read.csv(file = 'Data/StateAndCountyData.csv', header = TRUE)

# Split the observations for comparison
FEA_vc_split <- split(FEA_whole, FEA_whole$Variable_Code)
rm(FEA_whole)

###############################################################################
######## COMPARE SOME DATA BELOW...SOME THOUGHTS: Low Access Over Time ########
# Diabetes Rates Over Time # Diabetes Vs Low Access # Obesity Vs Low Access   #
############ Food Asst. Programs Vs. Diabetes and/or Obesity Rates ############
###############################################################################

# Compare Low Access between 2010-2015
l_access_10 <- FEA_vc_split$LACCESS_POP10
l_access_15 <- FEA_vc_split$LACCESS_POP15
# Determine the difference between he two sets
l_access_10_15 <- setdiff(l_access_10$ï..FIPS, l_access_15$ï..FIPS)
# Identify the index of rows to omit (i.e. set difference)
to_rem <- which(l_access_10$ï..FIPS %in% c(l_access_10_15))
rm(l_access_10_15)
# Remove rows not observed in other set
l_access_10_r <- l_access_10[-c(to_rem), ]
# Save some memory
rm(l_access_10)
rm(to_rem)
# Plot to pdf
l_access_plt <- plot(l_access_10_r$Value, l_access_15$Value)
dev.copy(pdf, 'l_access.pdf')
dev.off()
# Clean up the environment
rm(l_access_10_r)
rm(l_access_15)
rm(l_access_plt)

# Compare Diabetes percent between 2008-2013
diab_08 <- FEA_vc_split$PCT_DIABETES_ADULTS08
diab_13 <- FEA_vc_split$PCT_DIABETES_ADULTS13
# Determine the difference between the two sets
diab_08_13 <- setdiff(diab_13$County, diab_08$County)
# Identify the indexes of rows to omit (i.e. set difference)
to_rem <- which(diab_13$County %in% c(diab_08_13))
rm(diab_08_13)
# Remove the rows not observed in other set
diab_13_r <- diab_13[-c(to_rem), ]
# Save some memory
rm(diab_13)
rm(to_rem)
# Plot to pdf
pct_diabetes_plt <- plot(diab_08$Value, diab_13_r$Value)
dev.copy(pdf, 'pct_diabetes.pdf')
dev.off()
# Clean up the environment
rm(diab_13_r)
rm(diab_08)
rm(pct_diabetes_plt)

# Compare Diabetes percent between 2008-2013
snap_12 <- FEA_vc_split$PCT_SNAP12
diab_13 <- FEA_vc_split$PCT_DIABETES_ADULTS13
# Determine the difference between the two sets
diab_snap_12 <- setdiff(snap_12$ï..FIPS, diab_13$ï..FIPS)
# Identify the indexes of rows to omit (i.e. set difference)
to_rem <- which(snap_12$ï..FIPS %in% c(diab_snap_12))
rm(diab_snap_12)
# Remove the rows not observed in other set
snap_12_r <- snap_12[-c(to_rem), ]
# Save some memory
rm(snap_12)
rm(to_rem)
# Plot to pdf
snap_diabetes_plt <- plot(log10(snap_12_r$Value), log10(diab_13$Value))
dev.copy(pdf, 'snap_diabetes.pdf')
dev.off()
# Clean up the environment
rm(snap_12_r)
rm(diab_13)
rm(snap_diabetes_plt)

# Compare Low Access vs Diabetes rates 2010/2013
diab_13 <- FEA_vc_split$PCT_DIABETES_ADULTS13
l_access_10 <- FEA_vc_split$PCT_LACCESS_POP10
# Determine the difference between he two sets
diab_access_13 <- setdiff(l_access_10$ï..FIPS, diab_13$ï..FIPS)
# Identify the index of rows to omit (i.e. set difference)
to_rem <- which(l_access_10$ï..FIPS %in% c(diab_access_13))
rm(diab_access_13)
# Remove rows not observed in other set
l_access_10_r <- l_access_10[-c(to_rem), ]
# Save some memory
rm(l_access_10)
rm(to_rem)
# Plot to pdf
diab_access_plt <- plot(diab_13$Value, l_access_10_r$Value)
dev.copy(pdf, 'diab_access.pdf')
dev.off()
# Clean up the environment
rm(diab_13)
rm(l_access_10_r)
rm(diab_access_plt)

# Compare Low Access vs Obesity Rates 2010/2012
obese_12 <- FEA_vc_split$PCT_OBESE_ADULTS12
l_access_10 <- FEA_vc_split$PCT_LACCESS_POP10
# Determine the difference between he two sets
obese_access_12 <- setdiff(l_access_10$ï..FIPS, obese_12$ï..FIPS)
rm(obese_access_12)
# Plot to pdf
obese_access_plt <- plot(obese_12$Value, l_access_10$Value)
dev.copy(pdf, 'obese_access.pdf')
dev.off()
# Clean up the environment
rm(obese_12)
rm(l_access_10)
rm(obese_access_plt)