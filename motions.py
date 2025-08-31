from pybricks.tools import wait

async def move1(motorLeft,motorRight):
    print("move start")

    motorLeft.run(500)
    motorRight.run(500)
    await wait(1500)

    motorLeft.run(300)
    motorRight.run(500)
    await wait(1500)

    motorLeft.run(600)
    motorRight.run(400)
    await wait(3800)

    motorLeft.run(500)
    motorRight.run(500)
    await wait(450)

    motorLeft.run(600)
    motorRight.run(400)
    await wait(500)

    motorLeft.run(500)
    motorRight.run(500)
    await wait(2600)

    motorLeft.hold()
    motorRight.hold()

    motorLeft.run(-400)
    motorRight.run(-400)
    await wait(500)

    motorLeft.hold()
    motorRight.hold()

    motorLeft.run(-400)
    motorRight.run(400)
    await wait(800)

    motorLeft.hold()
    motorRight.hold()

    motorLeft.stop()
    motorRight.stop()
