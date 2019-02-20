# Define UI for application that draws a histogram
# ui <- fluidPage(
#   titlePanel("Drag-and-drop RAW to mzML converter"),
#   sidebarLayout(
#     sidebarPanel(
#       fileInput("rawFile", "Upload Thermo raw file",
#                 multiple = FALSE,
#                 accept = c(".raw")),
#       actionButton("QC", "Run Converter")
#     ),
    
#     mainPanel(
#       textOutput('text'),
#       plotOutput('TICplot'),
#       plotOutput('PSMplot')
#     )
#   )
# )

#https://gist.github.com/fbreitwieser/e6459659182486c5b7060f2e43435ec7
library(shiny)
jsfile <- "https://gist.githubusercontent.com/fbreitwieser/e6459659182486c5b7060f2e43435ec7/raw/c7e359ebce8f2e0a9e96c6e6fd1d696a5256009a/getdata.js"
cssfile <- "https://gist.githubusercontent.com/fbreitwieser/e6459659182486c5b7060f2e43435ec7/raw/b86a531d7d1f1628501772df0ea680b39be9dd59/styles.css"
ui <- shinyUI(
  fluidPage(
    tags$head(tags$link(rel="stylesheet", href=cssfile, type="text/css"),
              tags$script(src=jsfile)),
    sidebarLayout(
      sidebarPanel(
        h3(id="data-title", "Drop Datasets"),
        div(class="col-xs-12", id="drop-area", ondragover="dragOver(event)", 
            ondrop="dropData(event)")
      ),
      mainPanel(
        uiOutput('tables')
      )
    )

  )
)