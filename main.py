import mapreader, overlord, time
import pygamegui as gui


gui.StartPygame()
gui.DrawMap()
mapreader.InitMapBlocks()
gui.Update()

overlord.overlord.SpawnAgents()
overlord.overlord.OperationCharcoal(9, 4, 1)
while True:
    overlord.overlord.UpdateAgents()
    gui.Update()
    gui.clock.tick(gui.FPS)