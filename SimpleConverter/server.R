options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...

# Define server logic required to draw a histogram
server <- function(input, output) {
  observeEvent(input$QC, {
    file.copy(system(paste('msconvert ', input$rawFile$datapath)), 'data.mxML', overwrite = TRUE)
  })
}