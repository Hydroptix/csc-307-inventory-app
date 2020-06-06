import React, { Component } from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'


class App extends Component {
   state = {
      songs: [],
      playlists: []
   }
   
   removeSong = index => {
      const { songs } = this.state
      
      axios.delete("http://localhost:5000/songs/".concat(songs[index].id))

      this.setState({
         songs: songs.filter((song, i) => {
            return i !== index
         }),
      })
   }


   handleSubmit = playlist => {
      this.makePostCallPlaylist(playlist).then( callResult => {
         if (callResult.status === 201) {
            this.setState({ playlists: [...this.state.palylists, callResult.data] });
         }
      });
   }


   makePostCallPlaylist(playlist){
      return axios.post('http://localhost:5000/inventories', playlist)
       .then(function (response) {
         console.log(response);
         return response;
       })
       .catch(function (error) {
         console.log(error);
         return false;
       });
   }


   render() {
      const { songs } = this.state
      const { playlists } = this.state

      return (
        <div className="container">
          <Table songData={songs}
	      playlistData={playlists}
	      removeCharacter={this.removeCharacter} 
	      addSong={this.addSong} />

          <Form handleSubmit={this.handleSubmit} />
        </div>
      )
   }

   componentDidMount() {
      axios.get('http://localhost:5000/songs').then(res => {
          const songs = res.data.songs;
          this.setState({ songs });
      })
      .catch(function (error) {
          //Not handling the error. Just logging into the console.
          console.log(error);
      });
      axios.get('http://localhost:5000/inventories').then(res => {
	  const playlists = res.data.inventories;
	  this.setState({ playlists });
      })
      .catch(function (error) {
	  console.log(error);
      });
  }
}

export default App
