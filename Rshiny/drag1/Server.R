options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...

# Define server logic required to draw a histogram
# server <- function(input, output) {
#   observeEvent(input$QC, {
#     system(paste('msconvert ', input$rawFile$datapath, ' -v --mzML', sep=''))
#   })
# }

#https://gist.github.com/fbreitwieser/e6459659182486c5b7060f2e43435ec7
server <- function(input, output, session) {
  observeEvent(input$mydata, {
    len = length(input$mydata)
    output$tables <- renderUI({
      table_list <- lapply(1:len, function(i) {
        tableName <- names(input$mydata)[[i]]
        tableOutput(tableName)
      })
      do.call(tagList, table_list)
    })
    for (name in names(input$mydata)) {
      output[[name]] <- renderTable(read.csv(text=input$mydata[[name]]))
    }
  })
}