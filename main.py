import speedtest
import time

# This function will check you upload and download speed
def speedonly():
    test = speedtest.Speedtest()

    print(" Loading server List wait... ")
    test.get_servers()  # get list of servers

    print("Choosing best server wait...")
    # Here we choose the best server for test
    best = test.get_best_server()

    print(f"Found: {best['host']} located in {best['country']}")

    print(" Performing download test..")

    # Testing download data
    download_data = test.download()
    print(f"Download speed in Mbps:{download_data / (1024 * 1024)}")

    print(" Performing upload test...")
    # Testing Upload data
    upload_data = test.upload()
    print(f"Upload speed in Mbps:{upload_data / (1024 * 1024)}")


# This function will check your ping 10 times with delay of 3 seconds
def pingonly():
    print(" Checking Ping in ms:")
    # Checking Ping 6 times
    for i in range(10):
        test = speedtest.Speedtest()
        test.get_servers()
        test.get_best_server()
        ping_test = test.results.ping
        print(ping_test)
        time.sleep(3)


# Calling function pingonly
pingonly()
# calling funtion speedonly
speedonly()
