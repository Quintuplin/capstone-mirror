# Define UI for application that draws a histogram
ui <- fluidPage(
  
#   # Application title
#   titlePanel("Old Faithful Geyser Data"),
  
#   # Sidebar with a slider input for number of bins 
#   sidebarLayout(
#     sidebarPanel(
#       sliderInput("bins",
#                   "Number of bins:",
#                   min = 1,
#                   max = 50,
#                   value = 30)
#     ),
    
#     # Show a plot of the generated distribution
#     mainPanel(
#       plotOutput("distPlot")
#     )
#   )
# )

  titlePanel("Drag-and-drop RAW to mzML converter"),
  
  sidebarLayout(
    sidebarPanel(
      fileInput("rawFile", "Upload Thermo raw file",
                multiple = FALSE,
                accept = c(".raw")),

      # checkboxInput("AutoInfer", "AutoInfer parameters", TRUE),
      # txt = "My reactive title",
      # radioButtons("sep", "Standard",
      #              choices = c(HeLa = "HeLa",
      #                          UPS1 = "UPS1",
      #                          UPS2 = "UPS2",
      #                          Neeley = "Neeley"),
      #              selected = "HeLa"),

      # radioButtons('SpectaST', 'SpectraST version',
      #              choices = c('4.0' = '4',
      #                          '5.0' = '5'),
      #              selected = '5'),
     
      # radioButtons("depth", "QC depth",
      #              choices = c(Quick = 'Quick',
      #                          Full = 'Full'),
      #              selected = 'Quick'),
  
      actionButton("QC", "Run Converter")
    ),
    
    mainPanel(
      textOutput('text'),
      plotOutput('TICplot'),
      plotOutput('PSMplot')
    )
  )
)