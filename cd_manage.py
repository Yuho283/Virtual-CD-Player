from pprint import pprint
import discid
import musicbrainzngs

cd_data = {
    "Once upon a time in the pillows": {
        "artist": "the pillows",
        "year": "2009",
        "memo": "タワレコで買った。",
        "img": "PATH",
        "tracklist": ["GOOD DREAMS", "この世の果てまで", "バビロン天使の詩", "Thankyou, my twilight", "その未来は今", "ターミナルヘヴンズロック", "サードアイ", "RUSH", "アナザーモーニング", "Please Mr.Lostman", "MY FOOT"],
        "folder_path": "FOLDER_PATH",
    },
    "YELLOW DANCER": {
        "artist": "星野源",
        "year": "2015",
        "memo": "BOOKOFFにて購入。",
        "img": "PATH",
        "tracklist": ["時よ", "Week End", "SUN", "ミスユー", "Soul", "口づけ", "地獄でなぜ悪い", "Nerd Strut", "桜の森", "Crazy Crazy", "Snow Men", "Down Town", "夜", "Friend Ship"],
        "folder_path": "FOLDER_PATH",
    }
}

def load_and_write_cd():
    disc = discid.read()
    print(f"Disc ID:{disc}")
    musicbrainzngs.set_useragent("VirtualCDPlayer", "1.0", "noreply@example.com")
    try:
        result = musicbrainzngs.get_releases_by_discid(
            disc.id,
            includes=["artists", "recordings", "release-groups"]
        )
        title = result["disc"]["release-list"][0]["title"]
        artist = result["disc"]["release-list"][0]["artist-credit"][0]["artist"]["name"]
        date = result["disc"]["release-list"][0]["release-event-list"][0]["date"][:4]
        tracks = []
        for x in range(result["disc"]["release-list"][0]["medium-list"][0]["track-count"]):
            tracks.append(result["disc"]["release-list"][0]["medium-list"][0]["track-list"][x]["recording"]["title"])
        print(f"Result:\nTitle: {title}\nArtist: {artist}\nDate: {date}\nTracks: {tracks}")

    except musicbrainzngs.musicbrainz.ResponseError:
        print("MusicBrainzからCDが見つかりませんでした。")

def create_show_data(data, title):
    tracklist = ""
    idx = 1
    for track in data[title]["tracklist"]:
        tracklist += f"\n    {idx}: {track}"

        idx += 1
    show_data = f"""Name: {title}
Artist: {cd_data[title]["artist"]}
Year: {cd_data[title["year"]]}
Track: {tracklist}
Memo: {cd_data[title]["memo"]}
"""

    return show_data

load_and_write_cd()