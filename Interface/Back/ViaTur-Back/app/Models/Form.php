<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Form extends Model
{
    use HasFactory;

    public $table = 'fornecedores';
    protected $primaryKey = 'id';
    protected $fillable = ['phone','email','msg','name'];
    public $guarded = ['update_at','created_at','id'];
}
