import React from 'react'

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
