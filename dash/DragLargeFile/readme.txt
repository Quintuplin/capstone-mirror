INCOMPLETE

current drag and drop implementation utilizes dcc.upload
dcc.upload is not easily overridden and will immediately try to fill (read; overflow) system memory with large file contents
flask upload handles streaming, but does not have a built-in drag and drop

current expectation is that a third-party drag and drop (e.g. javascript) will handle drag and drop, with forwarding to flask