options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...

# Define server logic required to draw a histogram
server <- function(input, output) {
  
#   output$distPlot <- renderPlot({
#     # generate bins based on input$bins from ui.R
#     x    <- faithful[, 2] 
#     bins <- seq(min(x), max(x), length.out = input$bins + 1)
    
#     # draw the histogram with the specified number of bins
#     hist(x, breaks = bins, col = 'darkgray', border = 'white')
#   })
# }

  observeEvent(input$QC, {
    system(paste('msconvert ', input$rawFile$datapath, ' -v --mzML', sep=''))
    # QUERY <- '0'
    # query_file <- openMSfile('0.mzML')   # default filename  
    # make <- instrumentInfo(query_file)$manufacturer
    # model <- instrumentInfo(query_file)$model
    # output$text <- renderText({ paste('Query data is ', make, ' ', model, '.', sep='') })

    # reference_file <- openMSfile(paste(REFERENCE, '.mzML', sep=''))
    # reference_TIC <- tic(reference_file)
    # query_TIC <- tic(query_file)
    # output$TICplot <- renderPlot({
    #   plot(query_TIC[,1], query_TIC[,2], type="h", lwd=1, col='green', xlab='retention time (min)', ylab='total ion current') 
    #   lines(reference_TIC[,1], reference_TIC[,2], type="h", lwd=1, col='blue')
    # })

    # system(paste('spectrast -sL', SPECTRAST_LIBRARY, ' -sD', FASTA_FILE, ' -sTAA -sA! -s_HOM4 -sR! -sEpep.xml ', '0.mzML', sep = ''))
    # system(paste('xinteract -N', sub('$', '.interact.pep.xml', QUERY), ' -p0.95 -l7 -PPM -O -D', FASTA_FILE, ' ', QUERY, '.pep.xml', sep = ''))
    
    # system(paste('idconvert ', REFERENCE, '.interact.pep.xml', sep='')) 
    # system(paste('idconvert ', QUERY, '.interact.pep.xml', sep='')) 
    
    # query_ids <- openIDfile(paste(REFERENCE, '.mzid', sep='')) # omkastade for 1000 ng
    # reference_ids <- openIDfile(paste(QUERY, '.mzid', sep=''))
    
    # PSMs <- c(nrow(psms(reference_ids)), nrow(psms(query_ids)))
    # output$PSMplot <- renderPlot({ barplot(PSMs, names.arg=c('reference','query'), col=c("green","blue"), ylab='PSMs (p>=0.95)') })
  })
}