module.exports = {
	getRecords: async function(pool){
		let conn = await pool.getConnection();
		const rows = await conn.query("SELECT * FROM records WHERE date > NOW() - INTERVAL 1 HOUR"); 
		conn.end();
		return rows;
	}
}
