def replace_code(melody):
    return melody.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

def solution(m, musicinfos):
    m = replace_code(m)
    music = {}
    time = {}

    for musicinfo in musicinfos:
        start, end, title, melody = musicinfo.split(',')
        start_time = list(map(int, start.split(':')))
        end_time = list(map(int, end.split(':')))

        start_minutes = start_time[0] * 60 + start_time[1]
        end_minutes = end_time[0] * 60 + end_time[1]

        play_time = end_minutes - start_minutes
        time[title] = play_time

        melody = replace_code(melody)
        melody_length = len(melody)
        if melody_length > play_time:
            melody = melody[:play_time]
        elif melody_length < play_time:
            melody *= play_time // melody_length
            melody += melody[:play_time % melody_length]

        music[title] = melody

    answer = []
    for title, lyrics in music.items():
        if m in lyrics:
            answer.append([title, time[title]])

    if not answer:
        return "(None)"

    answer.sort(key=lambda x: x[1], reverse=True)
    return answer[0][0]
