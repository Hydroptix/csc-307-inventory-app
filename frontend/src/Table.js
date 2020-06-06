import React, { Component } from 'react'

// Table Header for songs in selected playlist
const TableHeader = () => {
   return (
     <thead>
       <tr>
	 <th>Song ID</th>
         <th>Artist</th>
         <th>Title</th>
	 <th>Genre</th>
	 <th>Duration</th>
	 <th>Cover Art</th>
       </tr>
     </thead>
     )
}

// Table Header for playlists
const TableHeader2 = () => {
   return (
     <thead>
       <tr>
	 <th>Playlist Name</th>
       </tr>
     </thead>
   )
}

// Table Body for songs in selected playlist
const TableBody = props => {
   const rows = props.songData.map((row, index) => {
     console.log(row)
     console.log(index)
      return (
        <tr key={index}>
	  <td>{row._id}</td>
          <td>{row.artist}</td>
          <td>{row.title}</td>
	  <td>{row.genre}</td>
	  <td>{row.durMin}:{row.durSec}</td>
	  <td>{row.image}</td>
	  <td>
	    <button onClick={() => props.removeCharacter(index)}>Add to Playlist</button>
	  </td>
          <td>
            <button onClick={() => props.removeCharacter(index)}>Delete</button>
          </td>
        </tr>
      )
   })

   return <tbody>{rows}</tbody>
}

// Table Body for playlists
const TableBody2 = props => {
   const rows = props.playlistData.map((row, index) => {
     console.log(row)
     console.log(index)
      return (
	<tr key={index}>
	  <td>{row.title}</td>
	  <td>
	    <button onClick={() => props.removeCharacter(index)}>Delete</button>
	  </td>
	  <td>
            <button onClick={() => props.removeCharacter(index)}>Select</button>
          </td>
	</tr>
      )
   })

   return <tbody>{rows}</tbody>
}
	      

const Table = props => {
   const { songData, playlistData, removeCharacter, addSong } = props
   
   return (
     <table>
       <TableHeader />
       <TableBody songData={songData} removeCharacter={removeCharacter} />
       <TableHeader2 />
       <TableBody2 playlistData={playlistData} removeCharacter={removeCharacter} />
     </table>

   )
}

export default Table
