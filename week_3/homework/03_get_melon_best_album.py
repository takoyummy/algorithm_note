genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    result = []
    total_dict = {}
    index_dict = {}
    for i in range(len(genre_array)):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in total_dict:
            total_dict[genre] = play
            index_dict[genre] = [[i, play]]
        else:
            total_dict[genre] += play
            index_dict[genre].append([i, play])
    total_dict2 = sorted(total_dict.items(), key=lambda item: item[1], reverse=True)
    for genre, play in total_dict2:
        index_array = index_dict[genre]
        sorted_index_array = sorted(index_array, key=lambda item: item[1], reverse=True)
        for i in range(len(sorted_index_array)):
            if i >1 :
                break
            result.append(sorted_index_array[i][0])

    return result


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!
