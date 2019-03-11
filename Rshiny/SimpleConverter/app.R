library(shiny)
library(mzR)

options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...
# setwd('C:/Users/nmpalmblad/Documents/Projects/Ben/')
my_output_dir <- ('C:/Users/quint/OneDrive/Desktop/folderfolder')

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
    #file.copy(system(paste('msconvert ', input$rawFile$datapath, ' -v --mzML', sep='')), "~/Desktop/folderfolder/x.txt" ,overwrite = TRUE)
    system(paste('C:/APPWin32bitBundle/APPServer/bin/pwiz/msconvert.exe ', input$rawFile$datapath, ' -o ', my_output_dir), intern = FALSE, ignore.stdout = TRUE, ignore.stderr = TRUE, wait = TRUE, show.output.on.console = TRUE, minimized = FALSE, invisible = FALSE)
    system('echo Done')
    }
  )}

  
shinyApp(ui, server)