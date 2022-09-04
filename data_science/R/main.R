# install package
install.packages('gapminder')

# load library
library(gapminder)

# peek at data
head(gapminder)

City <- c("New York", "San Francisco", "Boston", "Seattle")
State <- c("NY", "CA", "MA", "Seattle")
PopDensity <- c(26403, 18838, 13841, 7962)
densities <- data.frame(City, State, PopDensity)
City <- c("New York", "San Francisco", "Boston", "Seattle")
State <- c("NY", "CA", "MA", "Seattle")
PopDensity <- c(26403, 18838, 13841, 7962)
densities <- data.frame(City, State, PopDensity)
str(densities)
palette.pals()
palette.colors(palette = "Tableau 10")
string1 <-  r"("I no longer need to escape these " double quotes inside a quote," they said.)"
cat(string1)
x <- 1:5
y <- 6:10