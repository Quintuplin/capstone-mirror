options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...

# Define server logic required to draw a histogram
server <- function(input, output) {
  observeEvent(input$QC, {
    file.copy(input$rawFile$datapath, "~/Desktop/folderfolder/x.txt" ,overwrite = TRUE)
  })
}