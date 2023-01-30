from typing import *
from src.GameFunc.display.DisplayData import DisplayData, DisplayResolution
from src.GameFunc.player.PlayerBase import PlayerBase


import pygame

DOT = TypeVar("DOT", PlayerBase, DisplayData)  # 제네릭 타입 지원을 위한 TypeVar


class DisplayManager:
    def __init__(self, gui_data: Dict[str, Union[int, bool]], root_path: str, debug_mode: bool = False):
        # Display의 정보를 담고있는 Data Transfer Object를 생성하고 클래스 변수에 저장한다.
        self._display_data_object = DisplayData(
            screen_res = DisplayResolution.HD if gui_data.get("sc_res") == "hd" else DisplayResolution.FHD,
            screen_img_dir = f"{root_path}\\resources\\1920_1080_space.jpg",  # test background image
            cont = gui_data.get("continue")
        )
        self._debug_mode = debug_mode

    # 생성자 메소드를 통해 생성된 Display의 데이터를 담고있는 DTO에 접근하기 위해 Getter생성
    # DisplayData객체는 변경되지 않고 내부에 담고 있는 정보만 변경이 가능해야 하므로
    # 해당 클래스 변수의 Setter은 제작하지 않는다.
    @property
    def DisplayData(self) -> DisplayData:
        return self._display_data_object

    # 게임 화면에 전달받은 오브젝트들을 표시하는 메소드
    # @staticmethod
    # def DrawObject(screen: pygame.Surface, target_objects: List[DOT]):
    def DrawObject(self, screen: pygame.Surface, target_objects: List[DOT]):
        for target_object in target_objects:
            if isinstance(target_object, PlayerBase):  # target_object가 PlayerBase의 인스턴스인지 확인한다.
                # 플레이어의 애니메이션 적용을 위하여 플레이어의 스프라이트를 업데이트하는 메소드
                target_object.Sprite.UpdateSprite(move_data = target_object.MoveData)
                # 위에서 업데이트가 끝난 플레이어 스프라이트를 실제 게임화면에 그리는 메소드
                screen.blit(
                    target_object.Sprite.sprite_sf,
                    (
                        target_object.MoveData.X_Pos,
                        target_object.MoveData.Y_Pos
                    )
                )
                # 디버그 모드가 활성화 되면 화면 왼쪽상단에 데이터 확인용 텍스트가 생성된다.
                if self._debug_mode:
                    from src.tools.Debugger import Debbuger
                    Debbuger.DrawDebugText(sc_surf = screen, target_objects = [target_object])

                # 정지&움직임 상태 변수가 True일 경우 기본값인 False로 전환
                if target_object.MoveData.MovingStatus:
                    target_object.MoveData.MovingStatus = False

            elif isinstance(target_object, DisplayData):  # target_object가 DisplayData의 인스턴스인지 확인한다.
                # 배경화면의 Surface객체를 게임윈도우의 (0, 0)좌표에 그린다.
                screen.blit(target_object.ScreenImage, (0, 0))
