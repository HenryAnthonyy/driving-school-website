window.onload = function () {
	var chart = new CanvasJS.Chart("chartContainer", {

        animationEnabled: true,
        animationDuration: 6000,
        theme: "light2",
		title:{
			text: "Monthly Enrollments"           
		},
        axisY: {
            title: "Income"
        },
		data: [              
		{
			// Change type to "doughnut", "line", "splineArea", etc.
			type: "column",
			dataPoints: [
				{ y: 70000, label: "January" },
                { y: 80000,  label: "February" },
                { y: 90000,  label: "March" },
                { y: 85000,  label: "April" },
                { y: 95000,  label: "May" },
                { y: 100000, label: "June" },
                { y: 110000,  label: "July" },
                { y: 99000,  label: "August" },
                { y: 120000,  label: "September" },
                { y: 130000,  label: "October" },
                { y: 140000,  label: "November" },
                { y: 145000,  label: "December" }
			]
		}
		]
	});
	chart.render();
}


