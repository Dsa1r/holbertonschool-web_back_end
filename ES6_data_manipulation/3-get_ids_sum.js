export default function getStudentIdsSum (list){
return (list.reduce((acc , st) => st.id + acc , 0))

}