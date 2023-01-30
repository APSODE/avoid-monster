import pygame
from src.GameFunc.player.PlayerBase import PlayerBase
from src.GameFunc.display.DisplayData import DisplayData
from typing import *


T = TypeVar("T", PlayerBase, DisplayData)


class Debbuger:
    @staticmethod
    def _CreateDebugText(target_objects: List[T]) -> List[str]:
        display_target_text_list = []
        for target_object in target_objects:
            if isinstance(target_object, PlayerBase):
                # print("작동")
                player_move_data = target_object.MoveData
                player_sprite_data = target_object.Sprite

                # 플레이어 이동 데이터 확인 텍스트
                display_target_text_list.append(f"player move status : {player_move_data.MovingStatus}")
                display_target_text_list.append(f"player move direction : {player_move_data.Direction}")
                display_target_text_list.append(f"player current x pos : {player_move_data.X_Pos}")
                display_target_text_list.append(f"player current y pos : {player_move_data.Y_Pos}")
                display_target_text_list.append(f"player move x pos amount : {player_move_data.X_Move}")
                display_target_text_list.append(f"player move y pos amount : {player_move_data.X_Move}")
                display_target_text_list.append(f"player speed : {player_move_data.Speed}")

                # 플레이어 스프라이트 데이터 확인 텍스트
                player_current_sprite_key = "w" if player_move_data.MovingStatus else "s"
                player_current_sprite_num = player_sprite_data.SpriteNumData.get(player_current_sprite_key)
                player_current_sprite_max_num = player_sprite_data.SpriteNumData.get(player_current_sprite_key + "_M")
                display_target_text_list.append(f"player current sprite key : {player_current_sprite_key}\n")
                display_target_text_list.append(f"player current sprite num : {player_current_sprite_num}\n")
                display_target_text_list.append(f"player current sprite max num : {player_current_sprite_max_num}\n")

        return display_target_text_list

    @staticmethod
    def DrawDebugText(sc_surf: pygame.Surface, target_objects: List[T]):
        font = pygame.font.SysFont("arial", 30, True, False)
        text_object_list = []
        for data_text in Debbuger._CreateDebugText(target_objects = target_objects):
            text_object_list.append(
                font.render(
                    data_text,
                    True,
                    (0, 0, 0)
                )
            )
        count = 1
        for text_object in text_object_list:
            sc_surf.blit(text_object, (0, count * 30))
            count += 1

        pygame.display.update()
