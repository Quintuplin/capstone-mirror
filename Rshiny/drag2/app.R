# https://stackoverflow.com/questions/43819250/r-shiny-input-reactivity-error-on-drag-and-drop

library(plotly)
library(htmlwidgets)
library(shiny)
library(ggplot2)

ui <- shinyUI(fluidPage(

  tags$head(tags$script(type="text/javascript", src = "fileUp.js")),

  # DRAG AND DROP FILE INPUT
  h3(id="data-title", "Drop Datasets"),

  div(class="col-xs-12",id="drop-area",ondragover="dragOver(event)", 
      ondrop="dropData(event)",onClick="fallback(event)","Drop Area"),

  div(onClick="removeFiles(event)",
      actionButton(inputId="resetAutomaticInput",label="Reset Input"),
      verbatimTextOutput("inputdatafile"),
      verbatimTextOutput("rowsdatafile"),
      verbatimTextOutput("dataTable"))
)) 

server <- shinyServer(function(input, output) {

  observeEvent(input$datafile, {
    infile <- input$datafile
    if (length(infile)==0) {
      # User has not uploaded a file yet
        return(NULL)
    }    
    # CLEAN FILE
    name <- names(input$datafile)[length(infile)]
    csvFile <- reactive(
      if (length(input$datafile)>0){
        read.csv(text=input$datafile[[name]])
      }
    )

    output$dataTable <- renderPrint(csvFile())
    output$inputdatafile <- renderPrint(names(input$datafile))
    output$rowsdatafile <- renderPrint(sapply(input$datafile,nchar))

    output$hover <- h3({
    event <- event_data("plotly_hover")
    if (is.null(event)) "Hover events appear here (unhover to clear) " 
    else distrules[(event$pointNumber+1),-match("Dist", names(distrules))] 
    })
    
  })
})
shinyApp(ui, server)