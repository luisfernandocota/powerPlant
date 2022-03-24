# Django App
## Power Plant

This project consists of a test to apply for a job.

## Deploy
This project is deployed on a server under the following IP
```sh
164.92.78.73:8080
```

## Access to app
The url to access to admin django is **/admin/**
 >`user = username`
> `pass = password`

## APIS
The APIs contained in this project are the following

| API | PARAMS | URL |
| ------ | ------ | ------ |
| Get devices list | Params (name,type, status) | /api/devices/?parm=value |
| Get device | id_device  | /api/devices/{pk} |
| Get readings| Params(total=id_device)  | /api/readings/?total=pk |
| Get reading by device | id_device | /api/readings/device/{pk} |
| Get reading by type of device | id_type_device| /api/readings/device/type/{pk} |
| Get maintenances by device | id_device| /api/maintenances/device/{pk} |

