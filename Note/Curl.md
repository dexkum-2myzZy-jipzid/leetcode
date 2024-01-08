# Curl

Certainly! Here's a table summarizing some common usages of the `curl` command:

| **Action**                       | **Command**                                                  | **Description**                                              |
| -------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Simple GET Request               | `curl http://example.com`                                    | Retrieves data from the specified URL.                       |
| Download a File                  | `curl -o filename.html http://example.com`                   | Downloads the data to a specified file.                      |
| Follow Redirects                 | `curl -L http://example.com`                                 | Follows any redirects to the final destination.              |
| POST Request                     | `curl -X POST -d "param1=value1&param2=value2" http://example.com/resource` | Sends a POST request with data.                              |
| Upload a File                    | `curl -F "file=@path/to/local/file" http://example.com/upload` | Uploads a file to a server.                                  |
| Sending Headers                  | `curl -H "Content-Type: application/json" -X POST -d '{"key1":"value1"}' http://example.com/api` | Sends a request with additional header information.          |
| Basic Authentication             | `curl -u username:password http://example.com`               | Sends a request with basic HTTP authentication.              |
| Verbose Mode                     | `curl -v http://example.com`                                 | Provides detailed information about the request and response. |
| Save Headers and Body Separately | `curl -D headers.txt -o body.html http://example.com`        | Saves response headers and body in separate files.           |
| Use a Cookie                     | `curl -b "name=value" http://example.com`                    | Sends a request with a specified cookie.                     |

This table gives an overview of basic `curl` functionalities. Keep in mind that `curl` is very versatile, and these examples can be modified or combined to suit more specific needs. For a comprehensive list of all the options `curl` offers, consult the `curl` man page or the `curl --help` command.