export default function getStudentsByLocation (list , city) {
    return list.filter((st) => st.location === city )
    
}