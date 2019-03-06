# Define UI for application that draws a histogram
ui <- fluidPage(
  titlePanel("Simple upload RAW to mzML converter"),
  sidebarLayout(
    sidebarPanel(
      fileInput("rawFile", "Upload Thermo raw file",
                multiple = FALSE,
                accept = c(".raw")),
      actionButton("QC", "Run Converter")
    ),
    mainPanel(
      textOutput('text')
    )
  )
)