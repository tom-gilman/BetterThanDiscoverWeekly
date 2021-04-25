import os

from spotify_client import SpotifyClient


def main():

    #PUT API KEY HERE
    # instantiate spotify client
    #spotify_client = SpotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
    #                               os.getenv("SPOTIFY_USER_ID"))
    spotify_client = SpotifyClient("YOUR_API_TOKEN_HERE",
                                   "YOUR_USER_NAME_HERE")
    # get last played tracks10

    num_tracks_to_visualise = int(input("How many tracks would you like to view? "))
    last_played_tracks = spotify_client.get_last_played_tracks(num_tracks_to_visualise)

    print(f"\nHere are the last {num_tracks_to_visualise} tracks you listened to on your Spotify:")
    for index, track in enumerate(last_played_tracks):
        print(f"{index + 1}- {track}")

    # choose which tracks to use as a seed to generate a playlist
    indexes = input("\nEnter a list of up to 5 tracks you'd like to use as seeds. Use indexes separated by a space: ")
    indexes = indexes.split()
    seed_tracks = [last_played_tracks[int(index) - 1] for index in indexes]

    # get recommended tracks based off seed tracks
    recommended_tracks = spotify_client.get_track_recommendations(seed_tracks)
    print("\nHere are the recommended tracks which will be included in your new playlist:")
    for index, track in enumerate(recommended_tracks):
        print(f"{index + 1}- {track}")

    # get playlist name from user and create playlist
    playlist_name = input("\nWhat's the playlist name? ")
    playlist = spotify_client.create_playlist(playlist_name)
    print(f"\nPlaylist '{playlist.name}' was created successfully.")

    # populate playlist with recommended tracks
    spotify_client.populate_playlist(playlist, recommended_tracks)
    print(f"\nRecommended tracks successfully uploaded to playlist '{playlist.name}'.")


if __name__ == "__main__":
    main()
