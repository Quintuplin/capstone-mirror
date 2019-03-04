library(shiny)
library(mzR)

options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...
# setwd('C:/Users/nmpalmblad/Documents/Projects/Ben/')

ui <- fluidPage(

  titlePanel("msconvert"),
  
  sidebarLayout(
    sidebarPanel(
      fileInput("rawFile", "Upload Thermo raw file",
                multiple = FALSE,
                accept = c(".RAW")),
      
      actionButton("QC", "Run QC")
    ),
    
    mainPanel(
      textOutput('text')
    )
  )
)

server <- function(input, output) {

  observeEvent(input$QC, {
    file.copy(system(paste('msconvert ', input$rawFile$datapath, ' -v --mzML', sep='')), "~/Desktop/folderfolder/x.txt" ,overwrite = TRUE)
   
    }
  )}

  
shinyApp(ui, server)