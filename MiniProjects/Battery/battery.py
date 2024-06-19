import psutil

battery = psutil.sensors_battery()
percent = battery.percent
plugged = battery.power_plugged

if percent <= 30 and plugged != True:

    from pynotifier import Notification

    Notification(
        title="Battery Low",
        description=f"Battery is at {percent}%",
        duration=10

    ).send()

    