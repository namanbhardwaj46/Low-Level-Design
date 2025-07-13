from typing import Optional

from .products import *


class AudioPlayerFactory:

    @staticmethod
    def create_audio_player(type_: MediaFormat, volume: int, playBackRate: float) -> Optional[AudioPlayer]:
        return {
            MediaFormat.MP3: MP3Player,
            MediaFormat.WAV: WAVPlayer,
            MediaFormat.FLAC: FLACPlayer,
        }.get(type_)(volume, playBackRate)
