<!DOCTYPE html>
<html lang="ka">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buttons Example</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS -->
</head>
<body>
    <!-- ღილაკები -->
    <button class="btn primary">პირველი ღილაკი</button>
    <button class="btn primary">მეორე ღილაკი</button>
    <button class="btn secondary">მესამე ღილაკი</button>
    <button class="btn danger">მეოთხე ღილაკი</button>
</body>
</html>

/* საერთო ღილაკის სტილი */
.btn {
    padding: 10px 20px;
    font-size: 16px;
    border-radius: 5px;
    cursor: pointer;
    border: none;
    transition: all 0.3s ease;
}

/* პირველი და მეორე ღილაკი (primary) */
.primary {
    background-color: #4CAF50; /* მწვანე */
    color: white;
}

.primary:hover {
    background-color: #45a049; /* ღილაკი ჩრდილში წასვლისას */
}

/* მესამე ღილაკი (secondary) */
.secondary {
    background-color: #008CBA; /* ლურჯი */
    color: white;
}

.secondary:hover {
    background-color: #007bb5; /* ღილაკი ჩრდილში წასვლისას */
}

/* მეოთხე ღილაკი (danger) */
.danger {
    background-color: #f44336; /* წითელი */
    color: white;
}

.danger:hover {
    background-color: #e53935; /* ღილაკი ჩრდილში წასვლისას */
}


