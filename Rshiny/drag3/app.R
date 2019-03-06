library(shiny)
library(mzR)

options(shiny.maxRequestSize=5*1024^3)   # 5 GB maximum file size...

ui <- fluidPage(
    titlePanel("CofC_NIST raw to mzML converter mark 2"),
    sidebarLayout(
      sidebarPanel( "",
                    h1('Drag .raw file here')),
      mainPanel("main panel", 
                h1('The title of some text'), 
                p('And here is some content that is put into the first paragraph'),
                p(textOutput("here"))),
      imageOutput(outputId, width = "100%", height = "400px", click = NULL,
  dblclick = NULL, hover = NULL, hoverDelay = NULL,
  hoverDelayType = NULL, brush = NULL, clickId = NULL, hoverId = NULL,
  inline = FALSE),
      verbatimTextOutput('demo')
      
    )
)

server <- function(input, output) {
    output$dynamicText <- renderText({
        sprintf('You selected nothing')
    })
}

shinyApp(ui, server)