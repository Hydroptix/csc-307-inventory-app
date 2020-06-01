import React, { Component } from 'react'

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

const TableBody = props => {
   const rows = props.characterData.map((row, index) => {
      return (
        <tr key={index}>
	  <td>{row.song_id}</td>
          <td>{row.artist}</td>
          <td>{row.title}</td>
	  <td>{row.genre}</td>
	  <td>{row.durMin}:{row.durSec}</td>
	  <td>{row.imageURL}</td>
          <td>
            <button onClick={() => props.removeCharacter(index)}>Delete</button>
          </td>
        </tr>
      )
   })

   return <tbody>{rows}</tbody>
}

const Table = props => {
   const { characterData, removeCharacter } = props
   
   return (
     <table>
       <TableHeader />
       <TableBody characterData={characterData} removeCharacter={removeCharacter} />
     </table>
   )
}

export default Table
