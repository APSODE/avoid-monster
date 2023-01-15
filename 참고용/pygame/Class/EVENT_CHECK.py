import pygame

class EVENT:
    def EVENT_CHECK(NOW_EVENT):
        EVENT_TYPE = NOW_EVENT.type

        if EVENT_TYPE == pygame.QUIT:
            RUNNING_VALUE = False
            return RUNNING_VALUE

        else:
            RUNNING_VALUE = True
            return RUNNING_VALUE
