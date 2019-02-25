#
# This is the user-interface definition of a Shiny web application. You can
# run the application by clicking 'Run App' above.
#
# Find out more about building applications with Shiny here:
# 
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
shinyUI(fluidPage(
  
  # Application title
  titlePanel("Results"),
  
  # Sidebar just says "Hela" for now
  sidebarLayout(
    sidebarPanel("Hela"
      #sliderInput("bins",
      #            "Number of bins:",
      #            min = 1,
      #            max = 50,
      #            value = 30)
    ),
    
    # Show a plot of the generated distribution
    #mainPanel(
    #  tabsetPanel(
    #    tabPanel("Plot",plotOutput("distPlot")),
    #    tabPanel("Summary",verbatimTextOutput("summary"))
    #  ))
    fluidRow(column(12, offset = 0, "Pipeline",
                    fluidRow(column(2,offset= 1,"Sample"),
                             column(2,"LC"),
                             column(2,"Source"),
                             column(2,"MS-1"),
                             column(2,"MS-2")
                             ),
                    #Hard Coded colored squares for now
                    fluidRow(column(2,offset= 1,img(src="images/greenbox.png",width=100)),
                             column(2,img(src="images/greenbox.png",width=100)),
                             column(2,img(src="images/yellowbox.png",width=100)),
                             column(2,img(src="images/redbox.png",width=100)),
                             column(2,img(src="images/redbox.png",width=100))
                      
                    )
              )
       
             )
  )
))
