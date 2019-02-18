library(shiny)
library(mzR)

REFERENCE <- '2018-11-5_HeLa_OTOT'       # reference (could be local)
AMOUNT_INJECTED <- 200  
AMOUNT_INJECTED <- 200                   # ng HeLa injected (reference)
SPECTRAST_LIBRARY <- 'HeLa.splib'        # HeLa library
FASTA_FILE <- 'up000005640.fasta'        # sequence database

options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...
# setwd('C:/Users/nmpalmblad/Documents/Projects/Ben/')

ui <- fluidPage(

  titlePanel("ProteomeInvestigator QuickQC"),
  
  sidebarLayout(
    sidebarPanel(
      fileInput("rawFile", "Upload Thermo raw file",
                multiple = FALSE,
                accept = c("application/octet-stream",
                           "application/xml")),

      checkboxInput("AutoInfer", "AutoInfer parameters", TRUE),
      txt = "My reactive title",
      radioButtons("sep", "Standard",
                   choices = c(HeLa = "HeLa",
                               UPS1 = "UPS1",
                               UPS2 = "UPS2",
                               Neeley = "Neeley"),
                   selected = "HeLa"),

      radioButtons('SpectaST', 'SpectraST version',
                   choices = c('4.0' = '4',
                               '5.0' = '5'),
                   selected = '5'),
     
      radioButtons("depth", "QC depth",
                   choices = c(Quick = 'Quick',
                               Full = 'Full'),
                   selected = 'Quick')
      
      , actionButton("QC", "Run QC")
    ),
    
    mainPanel(
      textOutput('text'),
      plotOutput('TICplot'),
      plotOutput('PSMplot')
    )
  )
)

server <- function(input, output) {

  observeEvent(input$QC, {
    system(paste('msconvert ', input$rawFile$datapath, ' -v --mzML', sep=''))
    QUERY <- '0'
    query_file <- openMSfile('0.mzML')   # default filename  
    make <- instrumentInfo(query_file)$manufacturer
    model <- instrumentInfo(query_file)$model
    output$text <- renderText({ paste('Query data is ', make, ' ', model, '.', sep='') })

    reference_file <- openMSfile(paste(REFERENCE, '.mzML', sep=''))
    reference_TIC <- tic(reference_file)
    query_TIC <- tic(query_file)
    output$TICplot <- renderPlot({
      plot(query_TIC[,1], query_TIC[,2], type="h", lwd=1, col='green', xlab='retention time (min)', ylab='total ion current') 
      lines(reference_TIC[,1], reference_TIC[,2], type="h", lwd=1, col='blue')
    })
  
    # system(paste('spectrast -sL', SPECTRAST_LIBRARY, ' -sD', FASTA_FILE, ' -sTAA -sA! -s_HOM4 -sR! -sEpep.xml ', '0.mzML', sep = ''))
    # system(paste('xinteract -N', sub('$', '.interact.pep.xml', QUERY), ' -p0.95 -l7 -PPM -O -D', FASTA_FILE, ' ', QUERY, '.pep.xml', sep = ''))
    
    # system(paste('idconvert ', REFERENCE, '.interact.pep.xml', sep='')) 
    # system(paste('idconvert ', QUERY, '.interact.pep.xml', sep='')) 
    
    query_ids <- openIDfile(paste(REFERENCE, '.mzid', sep='')) # omkastade for 1000 ng
    reference_ids <- openIDfile(paste(QUERY, '.mzid', sep=''))
    
    PSMs <- c(nrow(psms(reference_ids)), nrow(psms(query_ids)))
    output$PSMplot <- renderPlot({ barplot(PSMs, names.arg=c('reference','query'), col=c("green","blue"), ylab='PSMs (p>=0.95)') })
    }
  )}

  
shinyApp(ui, server)
