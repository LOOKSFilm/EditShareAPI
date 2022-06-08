# EditShareAPI
This is a Python module for the Editshare API: https://developers.editshare.com/


## Install on Windows
Copy EditShareAPI to `.\Users\$USER\AppData\Local\Programs\Python\Python310\Lib\site-pakages`

### Dependencies
```
pip install requests
pip install urllib3
```

## Flow Metadata
https://developers.editshare.com/?urls.primaryName=EditShare%20FLOW%20Metadata

### Import
```Python
from EditShareAPI import FlowMetadata
```

### Login
```Python
flow = FlowMetadata("Server IP", "USER", "PASSWORD")
```
